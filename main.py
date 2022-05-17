from random import randint
import streamlit as st

def name_generator(N, syllables):
    names = []
    if N is None:
        N=10

    if syllables is None:
        syllables = 3
    prefix = ["de", "shaz", "ste", "zach", "za", "shiz", "rod", "cher", "char", "dar", "ever", "xan", "xe", "liz"]
    main = ["la", "bon", "dom", "bon", "sho", "ixi", "ca", "sam", "no", "na", "man", "liz"]
    suffix = ["ienne", "lea", "dea", "nea", "anne", "lee", "mae", "ine", "iana", "ela", "ena", "aela", "on", "lise", "liz"]

    def getrand(ls):
        return ls[randint(0, len(ls) - 1)]

    for i in range(int(N)):
        middle = "".join([getrand(main) for i in range(int(syllables) - 2)])
        name = name_mod = getrand(prefix) + middle + getrand(suffix)
        if "x" not in name:
            if randint(1, 3) == 3:
                name_mod = []
                for n in name:
                    name_mod.append(n)
                    if randint(1, 50) == 50:
                        name_mod.append("🍋")
        elif "z" not in name:
            if randint(1, 3) == 3:
                name_mod = []
                for n in name:
                    name_mod.append(n)
                    if randint(1, 100) == 100:
                        name_mod.append("zaela")
        name = "".join(name_mod)
        names.append(name)
    return names

header = st.empty()
slider_place_holder_number = st.empty()
slider_place_holder_syllables = st.empty()

if __name__ == '__main__':
    header = st.header("MALTA NAME GENERATOR")
    slider_place_holder_number = st.slider(min_value=5,max_value=100,label="Number of names to generate")
    slider_place_holder_syllables = st.slider(min_value=3, max_value=100,label="Number of syllables per name")
    names = name_generator(N=slider_place_holder_number,syllables=slider_place_holder_syllables)
    for name in names:
        st.write(name)
