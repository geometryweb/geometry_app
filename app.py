import streamlit as st

st.set_page_config(
    page_title= "pokemon",
    page_icon= "images\\monsterball.png"
)

st.title("포켓몬 도감")
st.text("포켓몬을 하나씩 추가해서 도감을 채워보세요")

st.markdown("""
            <style>
                img{
                   max-height: 300px 
                }
                .stElementContainer.element-container.st-emotion-cache-1j5ugxa.eiemyj1 div{
                    display: flex; /* 텍스트와 이미지를 한줄로 나란히 나열하기 */
                    justify-content: center;
                    font-size: 20px;
                }
                [data-testid=stExpanderToggleIcon] {
                    visibility: hidden; /* 확장 버튼 아래 꺽쇠 */
                }
                .st-emotion-cache-s1invk.enj44ev3 {
                    pointer-events: none; /* 확장 버튼 영역 */
                }
                .st-emotion-cache-80hqog.e1obcldf23 {
                    visibility: hidden; /* 확장 버튼 */
                }
                

            </style>
            """, unsafe_allow_html = True)

st.markdown("""
            <style>
                .add div{
                    display: flex;
                    font-size: 20px;
                    justify-content: center;
                    pointer-events; none;
                    visibility: hidden;
                }
            </style>
            
            """, unsafe_allow_html = True)
  

type_emoji_dict = {
    "노말": "⚪",
    "격투": "✊",
    "비행": "🕊",
    "독": "☠️",
    "땅": "🌋",
    "바위": "🪨",
    "벌레": "🐛",
    "고스트": "👻",
    "강철": "🤖",
    "불꽃": "🔥",
    "물": "💧",
    "풀": "🍃",
    "전기": "⚡",
    "에스퍼": "🔮",
    "얼음": "❄️",
    "드래곤": "🐲",
    "악": "😈",
    "페어리": "🧚"
}

initial_pokemons = [
    {
        "name": "피카츄",
        "types": ["전기"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/pikachu.webp"
    },
    {
        "name": "누오",
        "types": ["물", "땅"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/nuo.webp",
    },
    {
        "name": "갸라도스",
        "types": ["물", "비행"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/garados.webp",
    },
    {
        "name": "개굴닌자",
        "types": ["물", "악"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/frogninja.webp"
    },
    {
        "name": "루카리오",
        "types": ["격투", "강철"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/lukario.webp"
    },
    {
        "name": "에이스번",
        "types": ["불꽃"],
        "image_url": "https://storage.googleapis.com/firstpenguine-coding-school/pokemons/acebun.webp"
    },
]

example_pokemon={
    "name": "알로라 디그다",
    "types": ["땅", "강철"],
    "image_url": "https://i.namu.wiki/i/ulhBocfKW4GlOzn-eTmR-Fuicb5AkprEkvihlEDeqcGF2JwNq_5A_ZePPzSH_84ySvIohBVO_fElqYj5e1tyzNe3LYoaXshfcJ9HsrKNThiwTUkSDEL8f7vF2PQtmnLtEX_EbszJcR3Q1dpdnQyLcw.webp"
}

if "pokemons" not in st.session_state:
    st.session_state.pokemons = initial_pokemons
    
auto_complete = st.toggle("예시 데이터로 채우기")
with st.form(key = "form"):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input(
            label = "포켓몬 이름",
            value = example_pokemon["name"] if auto_complete else ""
            )
        
    with col2:
        types = st.multiselect(
            label = "포켓몬 타입",
            options = list(type_emoji_dict.keys()),
            max_selections = 2,
            default = example_pokemon["types"] if auto_complete else []
        )
    image_url = st.text_input(
        label="이미지 주소 URL",
        value = example_pokemon["image_url"] if auto_complete else ""
        )
    
    submit = st.form_submit_button(label="Submit")
    
    if submit:
        if not name:
            st.error("이름을 입력하세요")
        elif types ==0:
            st.error("타입을 하나 이상 선택하세요")
        else:
            st.success("포켓몬을 추가할 수 있습니다")
            st.session_state.pokemons.append({
                "name" : name,
                "types": types,
                "image_url": image_url if image_url else ".\\images\\default.png"               
            })

    

    
for i in range(0, len(st.session_state.pokemons),3):
    row_pokemons = st.session_state.pokemons[i: i+3]
    cols=st.columns(3)
    for j in range(len(row_pokemons)):
        with cols[j]:
            pokemon = row_pokemons[j]
            with st.expander(label=f"**{i+j+1}. {pokemon["name"]}**", expanded= True):
                st.image(pokemon["image_url"])
                emoji = [f"{type_emoji_dict[x]} {x}" for x in pokemon["types"]]
                st.text(" / ".join(emoji))
                delete_button = st.button(label="삭제", key =i+j, use_container_width =True)
                if delete_button:
                    del st.session_state.pokemons[i+j]
                    st.rerun()
                