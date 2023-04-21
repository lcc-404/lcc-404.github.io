function doGet(e) {

	var params = e.parameter;

	var SpreadSheet = SpreadsheetApp.openById("18DLC3gQmkK9sQhAfQwrPfPTFAaGWjP206byYIA888to");
	var Sheet = SpreadSheet.getSheets()[0];
	var LastRow = Sheet.getLastRow();

	Sheet.getRange(LastRow+1, 1).setValue(params.name);
	Sheet.getRange(LastRow+1, 2).setValue(params.mail);
	Sheet.getRange(LastRow+1, 3).setValue(params.formid);

	for (var i = 1; i <= 3; i++) {
		Sheet.getRange(LastRow+1, 3+i).setValue(params["q" + i.toString()]);
	}

	return ContentService.createTextOutput(params.thank);
}

/*在Google Sheet电子表格中,将名字，邮箱，和表单ID添加到Google Sheet电子表格的新一行*/
