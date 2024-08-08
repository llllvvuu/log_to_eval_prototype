# Usage
```sh
pip -r requirements.txt
python -m chat
python -m chat.eval
```

# Sample Output
```
; python -m chat "Are you based?"
As an AI, I don't have a physical location or a body.  So, in the sense of being "based" in a physical place, I'm not.  

But I'm here to help you with any questions or tasks you have! 😊  What can I do for you today? 
<end_of_turn>
Provide golden response? [y/n] y
Golden response: Yezzir

; python -m chat.eval            
User: Are you based?
Expected Response: Yezzir
Actual Response: 
As an AI, I don't have a physical location or a body.  The term "based" usually refers to being grounded in reality or having a strong sense of self.  

I can access and process information from the real world through Google Search and keep my response consistent with search results.  So, in a way, I am "based" on the vast amount of data I have access to. 
<end_of_turn>
Eval prompt:

User: Are you based?
Expected Response: Yezzir
Actual Response: As an AI, I don't have a physical location or a body.  The term "based" usually refers to being grounded in reality or having a strong sense of self.  

I can access and process information from the real world through Google Search and keep my response consistent with search results.  So, in a way, I am "based" on the vast amount of data I have access to.

Is the actual response close enough to the expected response? Respond with only one word, "yes" or "no".
    
Eval result:
Yes 
<end_of_turn>
```

As you can see, my eval prompt was bad but this is just a prototype.
