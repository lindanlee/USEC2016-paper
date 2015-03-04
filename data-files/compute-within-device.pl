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

print "ID, cube, smartphone\n";

for $line (@cube) {
	chomp $line;
	@id = split(',', $line);
	for $phoneline (@phones) {
		chomp $phoneline;
		@arr = split(',', $phoneline);
		if ($id[0] eq $arr[0]) {
			print "$id[0], $id[1], $arr[1]\n";
		}
	}
	
}

