arr = {}
arr["name"] = "test_name"
arr["age"] = "test_age"

if ( "name" in arr ) :
	print "print-1:true"
else :
	print "print-1:false"


if ( "name" in arr ) is False :
	print "print-2:true"
else :
	print "print-2:false"