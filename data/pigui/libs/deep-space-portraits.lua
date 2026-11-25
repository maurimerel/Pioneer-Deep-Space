-- Deep Space optional portrait renderer. GPL-3.0.
local Image = require 'pigui.libs.image'
local Vector2 = _G.Vector2
local Portraits = {}
local catalog = {} -- Append only after assets are installed and validated.
local cache = setmetatable({}, { __mode = 'v' })

local function hash(seed)
    local h = 0
    local s = tostring(seed)
    for i = 1, #s do h = (h * 131 + s:byte(i)) % 2147483647 end
    return h
end

function Portraits.New(character)
    local matches = {}
    for _, entry in ipairs(catalog) do
        if entry.female == not not character.female and entry.armour == not not character.armour then
            matches[#matches + 1] = entry
        end
    end
    if #matches == 0 then return nil end
    local h = hash(character.seed)
    local entry = matches[h % #matches + 1]
    local images = cache[entry.id]
    if not images then
        local ok, result = pcall(function()
            return { neutral = Image.New(entry.neutral), blink = entry.blink and Image.New(entry.blink) or nil }
        end)
        if not ok then return nil end
        images = result
        cache[entry.id] = images
    end
    return { images = images, phase = (h % 5000) / 1000 }
end

function Portraits.Draw(portrait, size)
    if not portrait then return false end
    local t = os.clock() + portrait.phase
    local frame = portrait.images.neutral
    if portrait.images.blink and t % 5.3 < 0.13 then frame = portrait.images.blink end
    frame:Draw(Vector2(size))
    return true
end

return Portraits
