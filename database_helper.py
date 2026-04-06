# --------------------------------------------------
# SIMPLE DATABASE (IN MEMORY)
# --------------------------------------------------
# This is NOT a real database
# It is only for demonstration purposes
#
# In production:
# - Use PostgreSQL / MySQL / MongoDB
# --------------------------------------------------

companies = []
tenders = []


# Save a company
def save_company(company):
    print("Saving company...")
    companies.append(company)


# Get all companies
def get_all_companies():
    return companies


# Save a tender
def save_tender(tender):
    print("Saving tender...")
    tenders.append(tender)