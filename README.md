RAJ GROUP V19 — Deploy this repository using GitHub Pages Actions.

1. Create a private Google Spreadsheet and open Extensions > Apps Script.
2. Paste google-apps-script/Code.gs, save and deploy as Web app (Execute as: Me, Access: Anyone). WARNING: Anyone with the URL can access/edit the backup; do not use this for sensitive production data without authentication.
3. Copy the deployed /exec URL into the site Google Sheets Backup field and click Connect.
4. Replace RAJ_GROUP_Party_Master.xlsx in GitHub and commit to rebuild master-data.json.
5. Only filled UNIT3/UNIT4/WHD/HO rows sync; report history is read-only.
6. Browser keeps unsent changes pending and retries; successful server verification is required before Saved appears.
7. Google Apps Script and Sheets have quotas; 2–3 second delivery is best effort, not guaranteed.
