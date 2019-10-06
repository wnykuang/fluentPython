def tag(name, *content, cls=None, **attrs):
    if cls is not None:
        attrs['class'] = cls
    if attrs:
        attr_str = "".join(' {}="{}"'.format(attr, value)
                           for attr, value in sorted(attrs.items()))
    else:
        attr_str = ""
    if content:
        return '\n'.join('<{}{}>{}</{}>'.format(name, attr_str, c, name) for c in content)

    else:
        return "<{}{} />".format(name, attr_str)


print(tag('br'))
print(tag('p', 'hello'))
print(tag('p', 'hello', 'world', 'hello2'))
print(tag('p', 'hello', name=2))