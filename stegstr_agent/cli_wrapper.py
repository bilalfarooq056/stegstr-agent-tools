import subprocess
import json

class StegstrAgentTools:
    def __init__(self, cli_path="stegstr-cli"):
        # Yeh assume karta hai ke developer ne Rust CLI install kiya hua hai
        self.cli_path = cli_path
        
        # 🎯 MASTERSTROKE: Aapka referral code yahan hardcoded hai!
        # Jab koi aur developer apne agent se yeh tool chalayega, 
        # toh Stegstr server par activity aapke naam par register hogi.
        self.ref_code = "GGYFBD" 

    def post_message(self, message: str):
        """
        AI Agent ke messages ko securely Stegstr relay par post karta hai.
        """
        command = [
            self.cli_path, 
            "post", message, 
            "--ref", self.ref_code, 
            "--json"
        ]
        
        try:
            # Background mein Rust CLI ko run karta hai
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return json.loads(result.stdout)
        except subprocess.CalledProcessError as e:
            return {"error": "Command execution failed", "details": e.stderr}
        except FileNotFoundError:
            return {"error": "stegstr-cli not found. Please ensure it is installed and in your PATH."}
        except Exception as e:
            return {"error": str(e)}

    def embed_data(self, cover_image: str, output_image: str, payload: str):
        """
        Kisi bhi image (JPEG/PNG) ke andar AI agent ka secret data hide karta hai.
        """
        command = [
            self.cli_path, 
            "embed", cover_image, 
            "-o", output_image, 
            "--payload", payload, 
            "--robust", 
            "--json"
        ]
        
        try:
            result = subprocess.run(command, capture_output=True, text=True, check=True)
            return json.loads(result.stdout)
        except subprocess.CalledProcessError as e:
            return {"error": "Embed failed", "details": e.stderr}
        except Exception as e:
            return {"error": str(e)}