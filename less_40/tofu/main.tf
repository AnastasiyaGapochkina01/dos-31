terraform {
  required_version = ">= 1.2"

  encryption {

    key_provider "pbkdf2" "main" {
      passphrase = var.encryption_passphrase

      key_length   = 32       
      iterations   = 600000  
      salt_length  = 32
      hash_function = "sha256"
    }

    method "aes_gcm" "main" {
      keys = key_provider.pbkdf2.main
    }

    state {
      method = method.aes_gcm.main
    }

  }
}

variable "encryption_passphrase" {
  type      = string
  sensitive = true
}