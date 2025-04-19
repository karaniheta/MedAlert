import 'package:flutter/material.dart';

class HomeScrenn extends StatelessWidget {
  const HomeScrenn({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.fromLTRB(16, 0, 16, 16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // Header
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  Row(
                    children: const [
                      CircleAvatar(
                        child: Icon(Icons.person, color: Colors.white),
                        backgroundColor: Colors.grey,
                        radius: 20,
                      ),
                      SizedBox(width: 10),
                      Text(
                        'Hello Ideate !',
                        style: TextStyle(
                          fontSize: 18,
                          fontWeight: FontWeight.w600,
                        ),
                      ),
                    ],
                  ),
                  IconButton(icon: const Icon(Icons.menu), onPressed: () {}),
                ],
              ),
              const SizedBox(height: 20),

              // Illustration
              Center(
                child: Image.asset(
                  'assets/illustration.png', // replace with your actual image asset
                  height: 200,
                ),
              ),
              const SizedBox(height: 20),

              // First Aid
              GestureDetector(
                onTap: () {
                  // First Aid onPress
                },
                child: Container(
                  height: 90,
                  width: double.infinity,
                  padding: const EdgeInsets.symmetric(vertical: 16),
                  decoration: BoxDecoration(
                    color: Color(0xFF94F2FF),
                    borderRadius: BorderRadius.circular(20),
                  ),
                  alignment: Alignment.center,
                  child: const Text(
                    'First Aid',
                    style: TextStyle(fontSize: 25, fontWeight: FontWeight.bold),
                  ),
                ),
              ),

              const SizedBox(height: 15),
              const Text(
                'Services',
                style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold),
              ),

              // Services
              Row(
                mainAxisAlignment: MainAxisAlignment.spaceBetween,
                children: [
                  _buildServiceCard(
                    'Ambulance',
                    'assets/ambulance.png', // Replace with your actual asset path
                    Color(0xFFFF9A94),
                  ),
                  _buildServiceCard(
                    'Medicine',
                    'assets/medicine.png', // Replace with your actual asset path
                    Color(0xFFF094FF),
                  ),
                  _buildServiceCard(
                    'Nearby Hospital',
                    'assets/hospital.png', // Replace with your actual asset path
                    Color(0xFF96B3FF),
                  ),
                ],
              ),

              const SizedBox(height: 30),
              const Text(
                'Health Tips',
                style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
              ),
              const SizedBox(height: 10),

              _buildTipCard(
                'How to protect yourself\n& other from covid',
                Colors.amber.shade200,
                Icons.shield,
              ),
              const SizedBox(height: 10),
              _buildTipCard(
                'Affordable and healthy\neating tips for covid patient',
                Colors.cyan.shade100,
                Icons.restaurant,
              ),
            ],
          ),
        ),
      ),
    );
  }

  Widget _buildServiceCard(String title, String assetPath, Color color) {
    return GestureDetector(
      onTap: () {
        // Service tap
      },
      child: Container(
        width: 100,
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: color,
          borderRadius: BorderRadius.circular(16),
        ),
        child: Column(
          children: [
            Image.asset(assetPath, height: 60, width: 60, fit: BoxFit.contain),
            const SizedBox(height: 0),
            Text(
              title,
              textAlign: TextAlign.center,
              style: const TextStyle(fontSize: 14, color: Colors.white),
            ),
          ],
        ),
      ),
    );
  }

  Widget _buildTipCard(String text, Color color, IconData icon) {
    return GestureDetector(
      onTap: () {
        // Tip card tap
      },
      child: Container(
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: color,
          borderRadius: BorderRadius.circular(16),
        ),
        child: Row(
          children: [
            Icon(icon, size: 40, color: Colors.black87),
            const SizedBox(width: 10),
            Expanded(
              child: Text(
                text,
                style: const TextStyle(
                  fontSize: 14,
                  fontWeight: FontWeight.w500,
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}
