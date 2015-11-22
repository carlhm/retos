<?php

$path_in  = $argv[1];
$path_out = $argv[2];
$fr       = fopen($path_in,  'r');

$array_read = array(
    array( // A
        array(), // x
        array()  // y
    ),
    array( // B
        array(), // x
        array()  // y
    )
);

/* read */
while(($line = fgetcsv($fr)) !== FALSE)
{
    /* real value? */
    if(is_null(($true = array_search('TRUE', $line))) || !is_numeric($line[0]))
    {
        continue;
    }

    $ab = ($true > 2);
    $xy = ($true - 1) % 2;

    $array_read[$ab][$xy][] = $line[0];

}
fclose($fr);

/* write */
$write = 
    own_implode($array_read[0][0], $array_read[0][1], ',A') . 
    own_implode($array_read[1][0], $array_read[1][1], ',B') 
;
file_put_contents($path_out, $write);

function own_implode(array $x = array(), array $y = array(), $key = ',')
{
    $text = '';
    $size = count($x);
    
    if(count($y) > $size)
    {
        $size = count($y);
    }
    
    for($i = 0; $i < $size; $i++)
    {
        if(!isset($x[$i]))
        {
            $x[$i] = 0;
        }
        if(!isset($y[$i]))
        {
            $y[$i] = 0;
        }
        $text .= $x[$i] .','. $y[$i] . $key . \PHP_EOL;
    }
    
    return $text;
}
