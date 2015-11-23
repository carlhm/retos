<?php

$path_in  = $argv[1];
$path_out = $argv[2];
$fr       = fopen($path_in,  'r');

$pre_line = array(
    'n00,n01,A'. \PHP_EOL,
    'n10,n11,B'. \PHP_EOL,
);
$csv_out = '';

/* read & pre-write */
while(($csv_in_line = fgetcsv($fr)) !== FALSE)
{
    /* real value? */
    if(is_null(($true = array_search('TRUE', $csv_in_line))) || !is_numeric($csv_in_line[0]))
    {
        continue;
    }
    // A/B x/y
    $ab    = (int)($true > 2);
    $match = 'n'. $ab . (($true - 1) % 2) .'';
    
    if(!strpos($csv_out, $match))
    {
        $csv_out .= $pre_line[$ab];
    }
    // replace match -> code
    $csv_out = substr_replace($csv_out, $csv_in_line[0], strpos($csv_out, $match), strlen($match));

}

// clean no replace
$csv_out = str_replace(array('n00','n01','n10','n11'), array('0','0','0','0'), $csv_out);

fclose($fr);

file_put_contents($path_out, $csv_out);
