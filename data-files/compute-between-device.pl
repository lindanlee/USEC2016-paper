#!/usr/bin/perl

open (DAT, "cube.csv") or die "Cannot open file\n";

my @cube, @phones;

while (<DAT>) {
        push @cube, $_;
}

close(DAT);

open (DAT, "smartphone.csv");

while (<DAT>) {
	push @phones, $_;

}

close(DAT);

print "ID, VUR, device\n";

for $line (@cube) {
	chomp $line;
	print $line . ", cubetastic3000\n";
}

for $phoneline (@phones) {
	chomp $phoneline;
	@arr = split(',', $phoneline);
	$counter=0;
	for $blah (@cube) {
		chomp $blah;
		@id = split(',', $blah);
		if ($id[0] eq $arr[0]) {
			$counter++;
		}
	}
	if ($counter==0) {
			print "$phoneline, smartphone\n";
	}
}
	

