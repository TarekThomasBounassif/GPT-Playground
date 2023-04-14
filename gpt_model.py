import openai
import json

class GPTModel:


    def __init__(self, API_key:str, model_choice:str, temp:int = 0.5, top_p:int = 1, freq_p:int =  0, p_penalty:int = 0) -> None:
        self.engine = model_choice
        self.temp = temp
        self.top_p = top_p
        self.freq_p = freq_p
        self.p_penalty = p_penalty
        openai.api_key = API_key
    
    def send_completion_req(self, prompt_in:str, max_tokens:int) -> openai.Completion:
        return openai.Completion.create(
            engine=self.engine,
            prompt=prompt_in,
            max_tokens=max_tokens,
            temperature=self.temp,
            top_p=self.top_p,
            frequency_penalty=self.freq_p,
            presence_penalty=self.p_penalty
        )
    
    def get_completion_text(self, comp_in:openai.Completion) -> str:
        return comp_in["choices"][0]["text"]
    
    def get_json_resp_dict(self, comp_in:openai.Completion) -> dict:
        try:
            dict_out = json.loads(self.get_completion_text(comp_in))
        except:
            return None
        return dict_out

    
    
