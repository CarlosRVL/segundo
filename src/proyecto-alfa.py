"""
Esqueleto de un programa que haga algo, con el obtetivo de estudiar como
se debe dise~ar un software (e implementar).
Se obtendran parametros en linea de comandos, tambien en modo interactivo
Se revisaran los parametros para tomar algunas decisiones. 
El procesamiento se realizara con una clase principal y otras auxiliares
Utilizaremos un fichero a parte para los mensajes de comunicación con el 
usuario
Utilizaremos un fichero de configuracion
"""
import argparse  # Manejo de argumentos en linea de comandos

import coso

def main():
    """
    Funcion principal
    Tratamiento de la entrada de parametros de ejecución y ejecución secuencial.
    """
    parser = argparse.ArgumentParser()
    parser = argparse.ArgumentParser(description='%(prog)s : Hacer cosas...')
    parser.add_argument("-v", "--verbose", help="Mostrar información de depuración", action="store_true")
    parser.add_argument("-t", "--testnet", help="Ejecución en modo test", action="store_true")
    parser.add_argument("-p", "--payfile", help="Nombre del archivo en el que guardar las direcciones de pago.")
    parser.add_argument("cadena", help="Cadena de entrada para procesar")
    argumento = parser.parse_args()
    cadena=argumento.cadena
    TESTNET=argumento.testnet
    MAINNET=not argumento.testnet
    if argumento.verbose:
        VERBOSE = True
        print("Verbose signigica que se da más información.")

    lacosa = elcoso()
    lacosa.print_fecha_creacion()
    
### Llamar a funcion principal.###
if __name__ == "__main__":
    main()
