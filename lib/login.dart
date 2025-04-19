import 'package:flutter/material.dart';
import 'package:medalert/home.dart';
import 'signup.dart';

class LoginScreen extends StatelessWidget {
  const LoginScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 32),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.stretch,
            children: [
              // Top illustration
              Center(
                child: Image.asset(
                  'assets/login.png', // Make sure to add this in your assets
                  height: 200,
                ),
              ),
              const SizedBox(height: 24),

              // Login title
              const Text(
                'LOGIN',
                style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
              ),
              const SizedBox(height: 16),

              // Username/email/phone input
              TextField(
                decoration: InputDecoration(
                  hintText: 'Username',
                  border: OutlineInputBorder(),
                ),
              ),
              const SizedBox(height: 16),

              // Password input + forgot
              Stack(
                alignment: Alignment.centerRight,
                children: [
                  TextField(
                    obscureText: true,
                    decoration: InputDecoration(
                      hintText: 'Password',
                      border: OutlineInputBorder(),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 24),

              // Login button
              ElevatedButton(
                onPressed: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => const HomeScrenn()),
                  );
                  // TODO: Add login logic
                },
                style: ElevatedButton.styleFrom(
                  backgroundColor: Color(0xFF6C63FF),
                  padding: const EdgeInsets.symmetric(vertical: 10),
                ),
                child: const Text(
                  'LOGIN',
                  style: TextStyle(
                    fontWeight: FontWeight.bold,
                    fontSize: 20,
                    color: Colors.white,
                  ),
                ),
              ),
              const SizedBox(height: 16),

              // Don't have an account? Sign Up
              Row(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  const Text("Don't have an account? "),
                  GestureDetector(
                    onTap: () {
                      Navigator.push(
                        context,
                        MaterialPageRoute(
                          builder: (context) => const SignupScreen(),
                        ),
                      );
                    },
                    child: const Text(
                      'Sign Up',
                      style: TextStyle(
                        color: Color(0xFF6C63FF),
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 24),

              // OR separator
              Row(
                children: [
                  Expanded(child: Divider(color: Colors.grey.shade400)),
                  const Padding(
                    padding: EdgeInsets.symmetric(horizontal: 12),
                    child: Text('Or'),
                  ),
                  Expanded(child: Divider(color: Colors.grey.shade400)),
                ],
              ),
              const SizedBox(height: 24),

              // Emergency button
              ElevatedButton(
                onPressed: () {
                  // TODO: Add emergency logic
                },
                style: ElevatedButton.styleFrom(
                  backgroundColor: Colors.redAccent,
                  padding: const EdgeInsets.symmetric(vertical: 10),
                ),
                child: const Text(
                  'EMERGENCY',
                  style: TextStyle(
                    fontWeight: FontWeight.bold,
                    fontSize: 20,
                    color: Colors.white,
                  ),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
