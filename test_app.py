import         # 6. GET /api/export?format=cef
        res = self.client.get('/api/export?format=cef')
        self.assertEqual(res.status_code, 200)
        self.assertIn(b'CEF:0|SPECTRE-CTI', res.data)
    def test_authentication_workflow(self):
        # 1. Test Demo Admin Login
        res = self.client.post('/api/auth/login', json={
            'username': 'admin',
            'password': 'SpectreAdmin2026!'
        })
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertTrue(data['success'])
        self.assertEqual(data['user']['username'], 'admin')
        self.assertEqual(data['user']['role'], 'ADMIN')
        # 2. Check /api/auth/me
        me_res = self.client.get('/api/auth/me')
        self.assertEqual(me_res.status_code, 200)
        me_data = json.loads(me_res.data)
        self.assertTrue(me_data['authenticated'])
        self.assertEqual(me_data['user']['username'], 'admin')
        # 3. Test Logout
        logout_res = self.client.post('/api/auth/logout')
        self.assertEqual(logout_res.status_code, 200)
        me_res2 = self.client.get('/api/auth/me')
        self.assertFalse(json.loads(me_res2.data)['authenticated'])
        # 4. Test Registration of a new agent
        new_username = f"agent_test_{os.getpid()}"
        reg_res = self.client.post('/api/auth/register', json={
            'username': new_username,
            'email': f"{new_username}@threatlab.org",
            'password': 'SecretPass2026!',
            'full_name': 'Special Agent Test',
            'role': 'INVESTIGATOR',
            'department': 'Forensic Triage'
        })
        self.assertEqual(reg_res.status_code, 201)
        reg_data = json.loads(reg_res.data)
        self.assertTrue(reg_data['success'])
        self.assertEqual(reg_data['user']['username'], new_username)
        # 5. Test Invalid Login
        bad_res = self.client.post('/api/auth/login', json={
            'username': 'admin',
            'password': 'WrongPassword123'
        })
        self.assertEqual(bad_res.status_code, 401)
if __name__ == '__main__':
    unittest.main()