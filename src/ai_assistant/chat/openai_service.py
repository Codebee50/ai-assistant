from io import BytesIO
from openai import OpenAI
import json

import openai
from ..tools.prices import checkout_products, get_item_price, get_product_discount, get_product_names
from pydub import AudioSegment
from pydub.playback import play
import pygame
import tempfile
import os

class OpenAiChatService():
    def __init__(self, system_message, tools=[], model="gpt-4o-mini") -> None:
        self.openai = OpenAI()
        self.system_message = system_message
        self.tools = tools
        self.model = model
        
    def play_audio(self, file_path):
        pygame.mixer.init()
        pygame.mixer.music.load(file_path)
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        
        
    def talker(self, message):
        response = self.openai.audio.speech.create(
            model = "tts-1",
            voice="nova",
            input=message
        )
        
        with tempfile.NamedTemporaryFile(suffix=".mp3", delete=False) as temp_file:
            temp_file.write(response.content)
            temp_file_path = temp_file.name
        try:
            self.play_audio(temp_file_path)
        finally:
            try:
                os.unlink(temp_file_path)
            except:
                pass
 
            
    
    def handle_tool_call(self, message):
        tool_responses = []

        for tool_call in message.tool_calls:
            tool_name = tool_call.function.name
            arguments = json.loads(tool_call.function.arguments)

            if tool_name == 'product_price':
                product_name = arguments.get('product_name')
                price = get_item_price(product_name)
                response = {
                    "role": "tool", 
                    "content": json.dumps({"product_name": product_name, "price": price}),
                    "tool_call_id": tool_call.id
                }
                tool_responses.append(response)
            
            if tool_name == 'product_has_discount':
                product_name = arguments.get('product_name')
                discounted_price = get_product_discount(product_name)
                response = {
                    "role": "tool", 
                    "content": json.dumps({"product_name": product_name, "discounted_price": discounted_price}),
                    "tool_call_id": tool_call.id
                }
                tool_responses.append(response)
            
            if tool_name == 'available_products':
                available = get_product_names()
                response = {
                    "role": "tool", 
                    "content": json.dumps({"available_products": available}),
                    "tool_call_id": tool_call.id
                }
                tool_responses.append(response)
            
            if tool_name == 'checkout_products':
                product_names = arguments.get('product_names')
                payment_url, total = checkout_products(product_names)
                response = {
                    "role": "tool", 
                    "content": json.dumps({"payment_url": payment_url, "order_total": total}),
                    "tool_call_id": tool_call.id
                }
                tool_responses.append(response)
            
            if tool_name == 'validate_payment':
                payment_reference = arguments.get('payment_reference')
                
                # fake a validation
                response = {
                    "role": "tool", 
                    "content": json.dumps({"is_valid": payment_reference == "cd6094aa-de01-4594-8d37-14d18637d78c"}),
                    "tool_call_id": tool_call.id
                }
                tool_responses.append(response)
            
        return tool_responses
            
                
        
    def chat(self, message, history):
        messages = [{"role": "system", "content": self.system_message}] + history + [{"role": "user", "content": message}]
        response = self.openai.chat.completions.create(model=self.model, messages=messages, tools=self.tools)
        
        if response.choices[0].finish_reason == 'tool_calls':
            message= response.choices[0].message
            tool_responses = self.handle_tool_call(message)
            messages.append(message)
            messages.extend(tool_responses)
            response = self.openai.chat.completions.create(model=self.model, messages=messages)
        
        reply = response.choices[0].message.content
        history += [{"role":"assistant", "content":reply}]
        self.talker(reply)
        return reply