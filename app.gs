function doGet(e) {

	var params = e.parameter;

	var SpreadSheet = SpreadsheetApp.openById("18DLC3gQmkK9sQhAfQwrPfPTFAaGWjP206byYIA888to");
	var Sheet = SpreadSheet.getSheets()[0];
	var LastRow = Sheet.getLastRow();
	formid=Sheet.getRange(LastRow, 3).getValue()+1;

	Sheet.getRange(LastRow+1, 1).setValue(params.name);
	Sheet.getRange(LastRow+1, 2).setValue(params.mail);
	Sheet.getRange(LastRow+1, 3).setValue(params.formid);
	Sheet.getRange(LastRow+1, 4).setValue(params.musiclevel);

	Sheet.getRange(LastRow+1, 9).setValue("test");
	Sheet.getRange(LastRow+1, 10).setValue(params["q6" +"_m"]+params["q6"+"_r"]+params["q6" +"_c"]+params["q6" +"_i"]);


	for (var i = 9; i <= 12; i++) {
		
		Sheet.getRange(LastRow+1, 4+i).setValue(params["q" + i.toString()]);
	}

	return ContentService.createTextOutput(params.thank);
}

