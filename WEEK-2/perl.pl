=> #!/usr/bin/perl
=> use strict;
=> use CGI qw(:standard);
   print "<title> Nginx Data</title>;
   print "<link rel=\"stylesheet\" href=\"(bootstrap link">\n";
   

=> print header;
=> print start_html('First HTML Page');                     // Start_html => Instantiates html script
=> print "<p>Hello</p>"                                     // html <p> paragraph tag


=> my $bash_Command = '/var/cgi-bin/bash1.sh';              // Here it's locating to the directory where the bash1.sh the shell script
                                                               is situated. 

 open(my $pipe, '-|', $bash_Command) or die $!;              // open the bash script file or exit(die $!)

while(my $line = <$pipe>)
{
    print "<p>$line</p>\n";                                   // $line => refers to the lines in the shell script file. 
    print "<H1> Inside wiple loop <H1>";                     // shell scripts written to be executed.   
    print "<p id=\"$i\" class=\"collapse\"> $line </p>\n";
}

print end_html;                                             // ends the HTML Page similar to </html>
