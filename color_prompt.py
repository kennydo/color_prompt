import platform

colors = [
#    "0;30", # black, looks boring
    "1;31", # red
    "1;32", # green
    "1;33", # yellow
    "1;34", # blue
    "1;35", # purple
    "1;36", # cyan
    "1;37", # white
]

def hostname():
    return platform.node()

def hash_color(word):
    chars = list(word)
    ascii_sum = sum([ord(char) for char in chars])
    return colors[ascii_sum % len(colors)]

def half_split(word):
    half = len(word)/2
    return (word[0:half], word[half:])

def color_word(word):
    color = hash_color(word)
    return "\[\e[%sm\]%s\[\e[0m\]" % (color, word)

def color_host():
    host_halves = half_split(hostname())
    colored_host = "".join([color_word(half) for half in host_halves])
    return colored_host

def make_prompt():
    return "\\n%(time)s %(path)s\\n%(user)s%(host)s$ " % {
        "time": "\[\e[0;92m\][\\t]",
        "path": "\[\e[0;33m\]\w\[\e[0m\]",
        "user": "\[\e[0;90m\]\u@",
        "host": color_host()
            }

if __name__ == "__main__":
    print make_prompt()

