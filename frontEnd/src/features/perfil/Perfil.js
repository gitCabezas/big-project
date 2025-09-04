
import React, { useState, useEffect } from 'react';
import { Box, Typography, Paper, CircularProgress, Alert } from '@mui/material';

const Perfil = () => {
  const [userData, setUserData] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    const fetchProfile = async () => {
      const token = localStorage.getItem('token');
      if (!token) {
        setError('Token de autenticação não encontrado. Por favor, faça login novamente.');
        setLoading(false);
        return;
      }

      try {
        const response = await fetch('/api/users/profile/me', {
          headers: {
            'Authorization': `Bearer ${token}`,
          },
        });

        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.message || 'Falha ao buscar dados do perfil.');
        }

        const data = await response.json();
        setUserData(data);
      } catch (err) {
        setError(err.message);
      } finally {
        setLoading(false);
      }
    };

    fetchProfile();
  }, []);

  if (loading) {
    return (
      <Box sx={{ display: 'flex', justifyContent: 'center', mt: 4 }}>
        <CircularProgress />
      </Box>
    );
  }

  if (error) {
    return <Alert severity="error">{error}</Alert>;
  }

  return (
    <Paper elevation={3} sx={{ p: 3 }}>
      <Typography variant="h4" gutterBottom>
        Perfil do Usuário
      </Typography>
      {userData ? (
        <Box>
          <Typography variant="h6" sx={{ mt: 2 }}><strong>ID:</strong> {userData.id}</Typography>
          <Typography variant="h6" sx={{ mt: 2 }}><strong>Username:</strong> {userData.username}</Typography>
          <Typography variant="h6" sx={{ mt: 2 }}><strong>Email:</strong> {userData.email}</Typography>
        </Box>
      ) : (
        <Typography>Nenhum dado de usuário para exibir.</Typography>
      )}
    </Paper>
  );
};

export default Perfil;
