import 'dart:convert';
import 'package:http/http.dart' as http;

void main() async {
  final res = await http.get(Uri.parse("https://gist.githubusercontent.com/TaeKyungg2/dd77b00e3929e3feb64be5bd411096cf/raw/saying.json"));
  final data = jsonDecode(res.body);
  final dataList=data.map((data) => Said(data['text_kr'], data['text_en'], data['author_kr'], data['author_en'])).toList();
  print(dataList[4].text_kr);
  print(dataList[4].text_en);
  print(dataList[4].author_kr);
  print(dataList[4].author_en);
}
class Said{
  final String text_kr;
  final String text_en;
  final String author_kr;
  final String author_en;
  Said(this.text_kr, this.text_en, this.author_kr, this.author_en);
}