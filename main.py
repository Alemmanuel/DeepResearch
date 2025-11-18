from dotenv import load_dotenv
load_dotenv()

from src.deep_research import DeepResearchSystem

def main():
    drs = DeepResearchSystem()

    print("Deep Research activo. Escribe 'salir' para terminar.\n")

    while True:
        query = input("Pregunta: ")

        if query.lower().strip() == "salir":
            print("Cerrando Deep Research. Hasta luego.")
            break

        result = drs.research(query)

        print("\n========== GAIA ==========\n")
        print(f"{result['gaia_score']}%")

        print("\n========== REFERENCIAS ==========\n")
        for r in result["links"]:
            print("-", r)

        print("\n--------------------------------------------\n")

if __name__ == "__main__":
    main()
