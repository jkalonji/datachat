from transformers import AutoTokenizer, AutoModelForCausalLM  
tokenizer = AutoTokenizer.from_pretrained("llmware/bling-stable-lm-3b-4e1t-v0", trust_remote_code=True)  
model = AutoModelForCausalLM.from_pretrained("llmware/bling-stable-lm-3b-4e1t-v0", trust_remote_code=True)

print(model)
model.save_pretrained("./llmware_bling_stable_3b.ckpt")
print('modèle sauvegardé')