# tender_fetch_playwright.py

from playwright.sync_api import sync_playwright
import time


URL = "https://jnportal.ujn.gov.rs/postupci-svi"


def fetch_tenders():

    tenders = []

    with sync_playwright() as p:

        browser = p.chromium.launch(headless=False)

        page = browser.new_page()

        page.goto(URL)

        # Esperar a que cargue la tabla
        page.wait_for_timeout(5000)

        # Obtener todas las filas de la tabla
        rows = page.query_selector_all("table tbody tr")

        for row in rows:

            try:

                cols = row.query_selector_all("td")

                # Evitar filas vacías
                if len(cols) < 12:
                    continue

                contracting_authority = cols[0].inner_text().strip()
                procurement_name_en = cols[1].inner_text().strip()
                procurement_name = cols[2].inner_text().strip()
                reference_number = cols[3].inner_text().strip()
                tender_type = cols[4].inner_text().strip()
                procedure_type = cols[5].inner_text().strip()
                cpv = cols[6].inner_text().strip()
                estimated_value = cols[7].inner_text().strip()

                # AQUÍ ESTÁ LA FECHA
                publication_date = cols[8].inner_text().strip()

                publication_date = cols[8].inner_text().strip()

                # Saltar encabezados o filas vacías
                if (
                        procurement_name == "Назив набавке"
                        or publication_date == "Датум објаве"
                        or procurement_name == ""
                ):
                    continue

                nuts = cols[9].inner_text().strip()
                submission_deadline = cols[10].inner_text().strip()
                status = cols[11].inner_text().strip()

                tender = {
                    "contracting_authority": contracting_authority,
                    "procurement_name_en": procurement_name_en,
                    "procurement_name": procurement_name,
                    "reference_number": reference_number,
                    "type": tender_type,
                    "procedure_type": procedure_type,
                    "cpv": cpv,
                    "estimated_value": estimated_value,
                    "publication_date": publication_date,
                    "nuts": nuts,
                    "submission_deadline": submission_deadline,
                    "status": status
                }

                tenders.append(tender)

                print("=" * 60)
                print("TITLE:", procurement_name)
                print("PUBLICATION DATE:", publication_date)
                print("DEADLINE:", submission_deadline)

            except Exception as e:

                print("Error processing row:", e)

        browser.close()

    return tenders


if __name__ == "__main__":

    data = fetch_tenders()

    print(f"\nTotal tenders fetched: {len(data)}")