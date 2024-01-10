"""
Script en Python que permite generar de rapidamente passwords seguras para multiples usos.
"""

# RECORDATORIO
# El script debe permitir al usuario poder generar passwords de diversa complejidad, permitiendo:
# - Seleccionar longitud password.
# - Facil de leer (solo letras)
# - Facil de recordar (letras y numeros)
# - Maxima seguridad (letras, numeros y caracteres especiales)


# IMPORTS ----

#import os
import re
import secrets
import string


# COMPLEXITY PATTERNS

LEVEL1_CMPLXITY_PATTERN = r"^[A-Z0-9]+$"
LEVEL2_CMPLXITY_PATTERN = r"^[a-zA-Z0-9]+$"
LEVEL3_CMPLXITY_PATTERN = r"^[a-zA-Z0-9!@#$%^&*()-=_+`~{}\[\]:;\"'<>,.?\\/]+$"

LEVEL1_VALID_CHAR = string.ascii_uppercase + string.digits
LEVEL2_VALID_CHAR = string.ascii_letters + string.digits
LEVEL3_VALID_CHAR = string.ascii_letters + string.digits + string.punctuation


COMPLEXITY_PATTERNS = [LEVEL1_CMPLXITY_PATTERN,
                       LEVEL2_CMPLXITY_PATTERN,
                       LEVEL3_CMPLXITY_PATTERN]

COMPLEXITY_CHARS = [LEVEL1_VALID_CHAR,
                    LEVEL2_VALID_CHAR,
                    LEVEL3_VALID_CHAR]


# FUNCTIONS ----

def userOptions():
    
    """Summary:
            Funcion sin parametros que actua interactuando con el usuario que ejecuta el script.
            La funcion trata de obtener las preferencias del usuario para la generacion de la password.
       Args:
    
       Returns: 
            - len_pwd ==> entero que representa la longitud en caracteres de la password a generar.
            - pwd_complexity ==> entero que representa el nivel de complejidad de la password a generar.
    
    """

    len_pwd = int(input("Longitud (en caracteres) de la password a generar:"))
    pwd_complexity = int(input("""Complejidad de la password a generar:
                                    1. Fácil de leer (letras mayusculas y numeros)
                                    2. Fácil de recordar (letras y números)
                                    3. Máxima seguridad (letras, números y caracteres especiales)"""))
    
    pwd_complexity -= 1 # Utilizare este valor como indice para la lista de patrones
    return len_pwd, pwd_complexity


##########################


def passGenerator(len_pwd, pwd_complexity):
    
    """"Summary:
            Funcion parametrizada que se encarga de generar una password de manera pseudoaleatoria con las
            caracteristicas seleccionadas por el usuario.
    
        Args:
            - pwd_complexity ==> entero que representa el nivel de complejidad de la password a generar.
            
        Returns:
            - generated_pwd ==> password generada.
        
    """
    
    # Hago uso del patron definido como expresion regular para generar la password
    
    valid_chars = COMPLEXITY_CHARS[pwd_complexity]
    
    generated_pwd = ''.join(secrets.choice(valid_chars) for _ in range(len_pwd))
    

    return generated_pwd
    


if __name__ == '__main__':
    
    # Permito al usuario seleccionar las opciones de la password
    len_pwd, pwd_complexity = userOptions()
    selected_complexity_pattern = COMPLEXITY_PATTERNS[pwd_complexity]
    selected_complexity_pattern = re.compile(selected_complexity_pattern)
    
    user_selection = 0
    while user_selection != 2:
        # Se genera una password con las caracteristicas seleccionadas
        generated_key = passGenerator(len_pwd= len_pwd,
                                    pwd_complexity= pwd_complexity)
        print()
        if selected_complexity_pattern.fullmatch(generated_key):
            print("GENERATED KEY: {key}".format(key = generated_key))
            print()
            while user_selection != 2:
                user_selection = int(input("""
                                        1. GENERAR NUEVA CLAVE.
                                        2. ME QUEDO CON ESTA."""))
                print()
                
                if user_selection == 1:
                    break
                elif user_selection == 2:
                    print()
                    print("SELECTED KEY [ {key} ]".format(key = generated_key))
                    print()
                    break
                else:
                    print("Selecciona una opción válida.")
                    print()
                    continue
        
        else:
            # Si la password no es valida, se generara una nueva.
            continue
        
    