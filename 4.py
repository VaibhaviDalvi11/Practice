#creating chat bot using basic if-else 


bot: str = "Belle"
#print(f"Hello ! {bot} How are you doing today ?")


while True:
    user_input: str = input('You: ').lower()
    
    if user_input in ['hi','hii','hello', 'adios','nihao']:
        print(f"{bot}: Hey ! How are you?")
    elif user_input in ['can you tell me a joke?']:
        print(f"{bot} : Your Life ! HeHe Hehe")    
            
    else:
        print(f'Oops ! {bot} did not understood that')    
       