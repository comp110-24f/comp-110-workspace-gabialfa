def speak(sound: str, repeat: int) -> None:
    print(sound * repeat)

    speak(sound="woof", repeat=3)
    speak(sound="meow", repeat=2)

    print(sound)
