# TODO: Implement SharePoint File Import in epi2.py

## Tasks
- [x] Add SharePoint-related imports to epi2.py (office365 libraries)
- [x] Enhance carregar_dados() function to handle SharePoint authentication and file downloads
- [x] Implement logic to download estoque.xlsx, funcionarios.xlsx, and historico.xlsx from SharePoint
- [x] Load downloaded files into pandas DataFrames (df_estoque, df_funcionarios, df_historico)
- [x] Add error handling and fallback to local file selection if SharePoint fails
- [ ] Test the implementation (simulate SharePoint connection)
- [x] Update GUI to reflect loaded data and provide feedback to user
