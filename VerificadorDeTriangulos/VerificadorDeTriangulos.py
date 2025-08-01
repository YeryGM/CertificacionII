def verificar_un_triangulo():
    """Función que verifica un solo triángulo con manejo de errores"""
    while True:
        try:
            print("\nIngrese los 3 lados del triángulo:")
            lados = []
            for i in range(3):
                lado = float(input(f"Ingrese el lado {chr(65+i)}: "))  # 65 es 'A' en ASCII
                if lado <= 0:
                    raise ValueError("Los lados deben ser positivos")
                lados.append(lado)
            1
            # Verificar desigualdad triangular
            a, b, c = sorted(lados)  # Ordenamos para simplificar la comprobación
            if a + b <= c:
                raise ValueError("Estos lados no forman un triángulo válido (violan la desigualdad triangular)")
                
            return lados
            
        except ValueError as e:
            print(f"Error: {e}. Por favor intente nuevamente.")

def determinar_tipo(lados):
    """Determina el tipo de triángulo basado en sus lados"""
    a, b, c = lados
    if a == b == c:
        return "EQUILATERO"
    elif a == b or a == c or b == c:
        return "ISOSCELES"
    else:
        return "ESCALENO"

def main():
    print("VERIFICADOR DE TRIÁNGULOS")
    print("-------------------------")
    
    while True:
        # Verificar un triángulo
        lados = verificar_un_triangulo()
        tipo = determinar_tipo(lados)
        print(f"\nRESULTADO: El triángulo es {tipo}")
        
        # Preguntar si desea verificar otro triángulo
        continuar = input("\n¿Desea verificar otro triángulo? (S/N): ").strip().upper()
        if continuar != 'S':
            print("\nPrograma terminado. ¡Hasta luego!")
            break

if __name__ == "__main__":
    main()