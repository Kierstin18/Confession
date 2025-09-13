import streamlit as st

# Confession letter generator as a Streamlit app
def make_confession_letter(crush_name: str) -> str:
    letter = f"""Hi {crush_name},

I hope this letter doesn’t catch you by surprise, but I’ve been meaning to write this for quite some time. 
There are things I want to tell you that I can’t always express in casual conversations, 
so I thought maybe writing them down would be the best way.

Since the day I met you, you’ve made such a big difference in my life without even trying. 
You have this way of making everything around you feel lighter and happier. Whether it’s your smile, 
the way you talk, or simply your presence, I always find myself looking forward to seeing you. 
Even the smallest moments—like a quick conversation or a simple joke—stay with me far longer than you probably realize.

Little by little, I noticed myself caring more about you,
 thinking of you when something reminds me of your laugh, 
 or when I hear a song that makes me smile the way you do. 
 I realized it’s more than just admiration or friendship—it’s something deeper.
   I like you, not just for how amazing you are on the outside, but for the kind,
     genuine, and thoughtful person I’ve come to know.

I’ll be honest, it took me some courage to say this because I didn’t want to risk our friendship or make things awkward.
 But I believe that being honest about my feelings is something you deserve.
   You’re truly special to me, and I want you to know how much you mean in my life.

I don’t expect you to feel the same way right away, 
and I don’t want to pressure you into an answer.
 I just wanted you to know what’s been in my heart. No matter what happens,
 I’ll always be grateful for the happiness you bring me and for the chance to know someone as wonderful as you.

With all sincerity,
Kier
"""
    return letter


st.markdown("""
<style>
  .stTextInput>div>div>input {
    font-size: 1.2em;
    padding: 0.75em;
  }
  .stButton>button {
    font-size: 1.2em;
    padding: 0.75em 1.5em;
    width: 100%;
    margin-top: 0.5em;
  }
  @media (max-width: 600px) {
    .stTextInput>div>div>input, .stButton>button {
      font-size: 1.1em;
    }
  }
</style>
""", unsafe_allow_html=True)

st.title("Confession Letter Generator 💌")
st.write("Easily create and share a heartfelt confession letter!")

crush = st.text_input("Crush's name", "[Crush's Name]", help="Enter the name of your crush.")

generate = st.button("Generate Letter")

if generate:
  letter = make_confession_letter(crush)
  st.text_area("", letter, height=400, label_visibility="collapsed")
  st.download_button("Download as .txt", letter, file_name=f"confession_to_{crush.replace(' ', '_')}.txt", use_container_width=True)
  st.info("Long-press to copy the letter or use the download button to save and share!")
