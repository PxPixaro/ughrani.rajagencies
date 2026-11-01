RAJ GROUP V19 — Deploy this repository using GitHub Pages Actions.

1. Create a private Google Spreadsheet and open Extensions > Apps Script.
2. Paste google-apps-script/Code.gs, save and deploy as Web app (Execute as: Me, Access: Anyone). WARNING: Anyone with the URL can access/edit the backup; do not use this for sensitive production data without authentication.
3. Copy the deployed /exec URL into the site Google Sheets Backup field and click Connect.
4. Replace RAJ_GROUP_Party_Master.xlsx in GitHub and commit to rebuild master-data.json.
5. Only filled UNIT3/UNIT4/WHD/HO rows sync; report history is read-only.
6. Browser keeps unsent changes pending and retries; successful server verification is required before Saved appears.
7. Google Apps Script and Sheets have quotas; 2–3 second delivery is best effort, not guaranteed.


## V20 updates
- Double-click any UNIT3 / UNIT4 / WHD / HO input (including an empty cell) to open Gujarati choices. Space still expands PD/CR shortcuts, but no longer opens the choices menu.
- City is exclusively from the GUJARATI worksheet, column C (CITY NAME), of RAJ_GROUP_Party_Master.xlsx. Empty master City stays blank; imported report City / Not Found is ignored. City field is read-only in the grid.
- Edit GUJARATI column C for the corresponding English party name, replace RAJ_GROUP_Party_Master.xlsx in GitHub, commit, and wait for GitHub Actions to finish. Refresh the website to load updated master-data.json.
- Google Sheets backup, print, and Excel export logic unchanged.
