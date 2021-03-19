
// Filter by status

$status = sqlite("sql",$_SqlGrid, "sqlget=yes")
$data = ""
while not($_sqleol)
  $data = $data + sqlget("code") + sqlget("name") + sqlget("userdata") + $_Crlf
  sqlnext
Endwhile

// Filter by dificulty

$data = sqlite("sql","Select * from caches where difficulty = $d_difficulty","")

