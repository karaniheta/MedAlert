import 'package:flutter/material.dart';
import 'package:medalert/login.dart';
import 'package:medalert/splashscreen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  // This widget is the root of your application.
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'MedAlert',
      
      home: const Splashscreen(),
    );
  }
}

