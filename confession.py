def ensure_pyperclip():
    try:
        import pyperclip
        return pyperclip
    except ImportError:
        print("pyperclip not found. Installing now...")
        import subprocess, sys
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'pyperclip'])
        import pyperclip
        return pyperclip
# confession_app.py
def make_confession_letter(Madam: str) -> str:
        letter = f"""Hi {Madam},

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


def main():
    print("Confession letter creator\n" + "-"*26)
    crush = input("Enter your crush's name: ").strip()
    while not crush:
        print("Name cannot be blank. Please enter your crush's name.")
        crush = input("Enter your crush's name: ").strip()
    # Only ask for crush's name
    letter = make_confession_letter(crush)
    print("\n" + "="*60 + "\n")
    print(letter)
    print("="*60 + "\n")

    # Sharing options
    print("How would you like to share your letter?")
    print("1. Copy to clipboard (for chat, email, etc.)")
    print("2. Save to a text file")
    print("3. Both")
    print("4. Exit")
    choice = input("Choose an option (1/2/3/4): ").strip()

    did_copy = False
    did_save = False
    filename = f"confession_to_{crush.replace(' ', '_')}.txt"

    if choice in ('1', '3'):
        try:
            pyperclip = ensure_pyperclip()
            pyperclip.copy(letter)
            print("Letter copied to clipboard! You can now paste it anywhere.")
            did_copy = True
        except Exception as e:
            print("Could not copy to clipboard:", e)

    if choice in ('2', '3'):
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write(letter)
            print(f"Saved to {filename}")
            did_save = True
        except Exception as e:
            print("Could not save file:", e)

    if not (did_copy or did_save):
        print("No sharing action taken. Goodbye!")

if __name__ == "__main__":
    main()
