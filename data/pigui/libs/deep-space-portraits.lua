-- Deep Space optional portrait renderer. GPL-3.0.
-- V5 offers deterministic NPC outfits, with a classic fallback.
local Image = require 'pigui.libs.image'
local Vector2 = _G.Vector2
local Portraits = {}

local function imagePath(name)
    return 'deep-space/facegen/v5/' .. name .. '.png'
end

local catalog = {
    { id = 'operator_001', female = true, armour = false, neutral = 'deep-space/portraits/operator_001/neutral.png' },
    { id = 'commander_003', female = false, armour = false, neutral = 'deep-space/portraits/commander_003/neutral.png' },
    { id = 'explorer_004', female = true, armour = false, neutral = 'deep-space/portraits/explorer_004/neutral.png' },
    { id = 'pilot_005', female = true, armour = false, neutral = 'deep-space/portraits/pilot_005/neutral.png' },
    { id = 'engineer_006', female = false, armour = false, neutral = 'deep-space/portraits/engineer_006/neutral.png' },
}
-- Only add fully-dressed V5 images, never the experimental torso-only layers.
for hairstyle = 1, 3 do
    for uniform = 1, 3 do
        local id = 'female_hair_' .. hairstyle .. '_uniform_' .. uniform
        catalog[#catalog + 1] = { id = id, female = true, armour = false, neutral = imagePath(id) }
    end
end
for uniform = 1, 3 do
    local id = 'male_uniform_' .. uniform
    catalog[#catalog + 1] = { id = id, female = false, armour = false, neutral = imagePath(id) }
end

local cache = setmetatable({}, { __mode = 'v' })

local function hash(seed)
    local h = 0
    local s = tostring(seed)
    for i = 1, #s do h = (h * 131 + s:byte(i)) % 2147483647 end
    return h
end

function Portraits.New(character)
    -- Keep Pioneer original faces for player customization, armour and ambiguous gender.
    if type(character.female) ~= 'boolean' or character.armour then return nil end
    local desc = character.faceDescription
    if desc and type(desc.FEATURE_GENDER) == 'number'
        and (desc.FEATURE_GENDER % 2 == 1) ~= character.female then
        return nil
    end
    local matches = {}
    for _, entry in ipairs(catalog) do
        if entry.female == character.female and entry.armour == false then
            matches[#matches + 1] = entry
        end
    end
    if #matches == 0 then return nil end
    local h = hash(character.seed)
    local entry = matches[h % #matches + 1]
    local images = cache[entry.id]
    if not images then
        local ok, result = pcall(function()
            return { neutral = Image.New(entry.neutral) }
        end)
        if not ok then return nil end
        images = result
        cache[entry.id] = images
    end
    return { images = images }
end

function Portraits.Draw(portrait, size)
    if not portrait then return false end
    portrait.images.neutral:Draw(Vector2(size))
    return true
end

return Portraits
