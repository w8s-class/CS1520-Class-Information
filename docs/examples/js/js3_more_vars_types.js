function demo() {
	var i1, i2, f1, f2, si, sf;

	i1 = 10;
	i2 = 20;

	f1 = 1.5;
	f2 = 3.14;

	si = "5";
	sf = "5.5";

	document.writeln("i1 is:  ", i1, " and has type ", typeof(i1));
	document.writeln("<br />");
	document.writeln("i2 is:  ", i2, " and has type ", typeof(i2));
	document.writeln("<br />");
	document.writeln("f1 is:  ", f1, " and has type ", typeof(f1));
	document.writeln("<br />");
	document.writeln("f2 is:  ", f2, " and has type ", typeof(f2));
	document.writeln("<br />");
	document.writeln("si is:  ", si, " and has type ", typeof(si));
	document.writeln("<br />");
	document.writeln("sf is:  ", sf, " and has type ", typeof(sf));
	document.writeln("<br />");

	document.writeln("<br /><br />");

	document.writeln("parseInt(si) is:  ", parseInt(si), " and has type ", typeof(parseInt(si)));
	document.writeln("<br />");
	document.writeln("parseInt(sf) is:  ", parseInt(sf), " and has type ", typeof(parseInt(sf)));
	document.writeln("<br />");
	document.writeln("parseFloat(si) is:  ", parseFloat(si), " and has type ", typeof(parseFloat(si)));
	document.writeln("<br />");
	document.writeln("parseFloat(sf) is:  ", parseFloat(sf), " and has type ", typeof(parseFloat(sf)));
	document.writeln("<br />");

	document.writeln("<br /><br />");

	var s1, s2, s3;

	s1 = "a string";
	s2 = "a string";
	s3 = s1;

	document.write("s1 is ");
	if (s1 == s2) {
		document.write("equal to");
	}
	else if (s1 < s2) {
		document.write("less than");
	}
	else if (s1 > s2) {
		document.write("greater than");
	}
	document.write(" s2!");
	document.writeln("<br />");
	
	document.write("s1 is ");
	if (s1 == s3) {
		document.write("equal to");
	}
	else if (s1 < s3) {
		document.write("less than");
	}
	else if (s1 > s3) {
		document.write("greater than");
	}
	document.write(" s3!");
	document.writeln("<br />");
}
