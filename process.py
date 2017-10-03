def common_replace(a):

    a = a.replace(chr(8220), '"')
    a = a.replace(chr(8221), '"')
    a = a.lstrip().replace(chr(8226), "\n")
    a = a.replace(chr(63719), " ")
    if chr(8211) in a:
        # print('found - for ' + a )
        a = a.lstrip().replace(chr(8211), "")
        a += "\n"
        print(a)

    return a


def process_content(content):

    contents = content.splitlines()
    # contents = open('input').readlines()
    merged = ""
    # print(content)
    for content in contents[1:]:
    # replacing bullet points

        content = common_replace(content)

        merged = merged + " " + content

    contents[0] = common_replace(contents[0])
    merged = contents[0] + merged

    return merged