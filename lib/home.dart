import 'package:flutter/material.dart';
import 'package:medalert/profile.dart';
import 'package:medalert/Ambulance.dart';

class HomeScrenn extends StatelessWidget {
  const HomeScrenn({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        backgroundColor: Colors.white,
        elevation: 0,
        iconTheme: const IconThemeData(color: Colors.black),
        title: const Text(
          'Hello Ideate !',
          style: TextStyle(color: Colors.black, fontWeight: FontWeight.bold),
        ),
      ),
      drawer: Drawer(
        backgroundColor: const Color(0xFF333333),
        child: SafeArea(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Padding(
                padding: const EdgeInsets.symmetric(
                  horizontal: 20,
                  vertical: 20,
                ),
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceBetween,
                  children: [
                    const Text(
                      'Menu',
                      style: TextStyle(
                        color: Colors.white,
                        fontSize: 28,
                        fontWeight: FontWeight.bold,
                      ),
                    ),
                    GestureDetector(
                      onTap: () => Navigator.of(context).pop(),
                      child: const Icon(
                        Icons.close,
                        color: Colors.white,
                        size: 28,
                      ),
                    ),
                  ],
                ),
              ),
              const Divider(color: Colors.white54),
              ListTile(
                leading: const Icon(Icons.home, color: Colors.white),
                title: const Text(
                  'Home',
                  style: TextStyle(color: Colors.white),
                ),
                onTap: () {
                  Navigator.pop(context);
                },
              ),
              ListTile(
                leading: const Icon(Icons.person, color: Colors.white),
                title: const Text(
                  'Profile',
                  style: TextStyle(color: Colors.white),
                ),
                onTap: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(
                      builder: (context) => const ProfilePage(),
                    ),
                  );
                },
              ),
              ListTile(
                leading: const Icon(Icons.logout, color: Colors.white),
                title: const Text(
                  'Log Out',
                  style: TextStyle(color: Colors.white),
                ),
                onTap: () {
                  Navigator.pop(context);
                },
              ),
            ],
          ),
        ),
      ),
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.fromLTRB(16, 0, 16, 16),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
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
                    color: const Color(0xFF94F2FF),
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
              Padding(
                padding: const EdgeInsets.fromLTRB(5, 5, 5, 0),
                child: Row(
                  children: [
                    Expanded(
                      child: _buildServiceCard(
                        context,
                        'Ambulance Booking',
                        'assets/ambulance.png',
                        const Color(0xFFFF9A94),
                        const AmbulanceScreen(), // Navigate to AmbulanceScreen
                      ),
                    ),
                    const SizedBox(width: 16),
                    Expanded(
                      child: _buildServiceCard(
                        context,
                        'Medicine Order',
                        'assets/medicine.png',
                        const Color(0xFFF094FF),
                        null, // No navigation for now
                      ),
                    ),
                  ],
                ),
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
              const SizedBox(height: 20),
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

  Widget _buildServiceCard(
    BuildContext context,
    String title,
    String assetPath,
    Color color,
    Widget? navigateTo,
  ) {
    return GestureDetector(
      onTap: () {
        if (navigateTo != null) {
          Navigator.push(
            context,
            MaterialPageRoute(builder: (context) => navigateTo),
          );
        }
      },
      child: Container(
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: color,
          borderRadius: BorderRadius.circular(16),
        ),
        child: Column(
          children: [
            Image.asset(assetPath, height: 80, width: 100, fit: BoxFit.contain),
            const SizedBox(height: 10),
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
        width: double.infinity,
        height: 80,
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
