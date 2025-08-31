import 'dart:convert';
import 'package:http/http.dart' as http;

void main() async {
  final res = await http.get(Uri.parse("https://gist.githubusercontent.com/TaeKyungg2/dd77b00e3929e3feb64be5bd411096cf/raw/6bac064316eca99fec93d05d71f9edccfc04e96c/saying.json"));
  final data = jsonDecode(res.body);
  print(data[1]);
}