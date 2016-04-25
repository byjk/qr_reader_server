function parse_s4_barcode(barcode)
{ 
  a = {};
  if (barcode.indexOf('S4D') == 0)
  {
    s = barcode.slice(3);
    a = s.split('.');
    eval("a = {art_id: -1, doc_id: "+a[0]+", version_id: "+a[1]+"};");
  } 
  else if (barcode.indexOf('S4A') == 0 || barcode.indexOf('S4O') == 0)
  {
    s = barcode.slice(3);
    eval("a = {art_id: "+s+", doc_id: -1, version_id: -1};");
  } 
  return a
}

if (WScript.Arguments.Length > 0)
{
  s = WScript.Arguments(0);
  r = parse_s4_barcode(s);
  WScript.Echo(r.doc_id);  
}   

// eval("a = {doc_id:123, version_id: 321};");
// 
// WScript.Echo(a.version_id)
