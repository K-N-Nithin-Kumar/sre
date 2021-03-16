#!/usr/bin/perl

use CGI;
use List::MoreUtils qw(uniq);

my $cgi = new CGI;

print $cgi->start_html(
    -title=>'Nginx Log',
    -style => { -src => 'https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css' },
    -script => [
        { -src  => 'https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js' },                            
        { -src  => 'https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js' }
    ]
),
    $cgi->('Week 2 | Perl Task'), "\n";

#for each unique date, perform
@udate=uniq @dates;
print "<div class=\"container\"><div class=\"panel-group\" id=\"accordion\">\n";
for(my $i=0; $i <= $#udate; $i++){
    print "<div class=\"panel panel-default\">\n
      <div class=\"panel-heading\">\n
        <h4 class=\"panel-title\">\n
          <a data-toggle=\"collapse\" data-parent=\"#accordion\" data-target=\"#$i\">$udate[$i]</a>\n                     //Bootstrap code which is used to add collapsible button.
        </h4>\n
      </div>\n";
    $ext = `source day_summary.sh; high_req $udate[$i]`;
    print "<div id=\"$i\" class=\"panel-collapse collapse\">\n
        <div class=\"panel-body\">$ext</div>\n
      </div>\n
    </div>\n";
}
print "</div>\n";
=> print header;
=> print start_html('First HTML Page');                     // Start_html => Instantiates html script
=> print "<p>Hello</p>"                                     // html <p> paragraph tag


=> my $bash_Command = '/var/cgi-bin/bash1.sh';              // Here it's locating to the directory where the bash1.sh the shell script
                                                               is situated. 

 open(my $pipe, '-|', $bash_Command) or die $!;              // open the bash script file or exit(die $!)

while(my $line = <$pipe>)
{
    print "<p>$line</p>\n";                                   // $line => refers to the lines in the shell script file. 
    print "<H1> Inside while loop <H1>";                     // shell scripts written to be executed.   
    print "<p id=\"$i\" class=\"collapse\"> $line </p>\n";
}

print end_html;                                             // ends the HTML Page similar to </html>

