r, g, b = io.read("*n", "*n", "*n")
if r > g and r > b then
    print('raudur')
elseif g > r and g > b then
    print('graenn')
elseif b > r and b > g then
    print('blar')
elseif r == g and b < g then
    print('gulur')
elseif r == b and g < b then
    print('fjolubleikur')
elseif b == g and r < b then
    print('blagraenn')
elseif r == g and g == b and b == 0 then
    print('svartur')
elseif r == g and g == b and b == 255 then
    print('hvitur')
elseif r == g and g == b then
    print('grar')
else
    print('othekkt')
end
