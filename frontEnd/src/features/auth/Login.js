
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import {
  Button,
  TextField,
  Box,
  Typography,
  Grid,
  Link as MuiLink,
} from '@mui/material';
import logo from '../../Logo_FC_sem_fundo.png';

const Login = () => {
  const navigate = useNavigate();
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleSubmit = async (event) => {
    event.preventDefault();
    setError('');

    try {
      const response = await fetch('/api/auth/login', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, password }),
      });

      if (response.ok) {
        const data = await response.json();
        localStorage.setItem('token', data.token);
        navigate('/clientes');
      } else {
        const errorData = await response.json();
        setError(errorData.message || 'Credenciais inválidas');
      }
    } catch (err) {
      setError('Falha ao conectar ao servidor. Tente novamente mais tarde.');
    }
  };

  return (
    <Box
      sx={{
        display: 'flex',
        justifyContent: 'center',
        alignItems: 'center',
        minHeight: '100vh',
        bgcolor: 'background.default',
        p: 2, // Padding around the main grid
      }}
    >
      <Grid container sx={{ maxWidth: '1200px', bgcolor: 'white', borderRadius: 2, overflow: 'hidden' }}>
        {/* Left Column: Image */}
        <Grid
          item
          xs={false} // Hidden on extra-small screens
          sm={6}
          md={7}
          sx={{
            display: 'flex',
            justifyContent: 'center',
            alignItems: 'center',
            p: 4,
          }}
        >
          <img src="/logo512.png" alt="Company Logo" style={{ maxWidth: '80%', height: 'auto' }} />
        </Grid>

        {/* Right Column: Form */}
        <Grid item xs={12} sm={6} md={5}>
          <Box
            sx={{
              p: { xs: 3, md: 6 },
              display: 'flex',
              flexDirection: 'column',
              alignItems: 'center',
              justifyContent: 'center',
              height: '100%',
            }}
          >
            <Typography component="h1" variant="h5">
              Bem-vindo de volta!
            </Typography>
            <Typography variant="body2" color="text.secondary" sx={{ mb: 3 }}>
              Faça login em sua conta para continuar.
            </Typography>
            <Box component="form" noValidate onSubmit={handleSubmit} sx={{ mt: 1, width: '100%' }}>
              <TextField
                margin="normal"
                required
                fullWidth
                id="username"
                label="Nome de Usuário"
                name="username"
                autoComplete="username"
                autoFocus
                variant="standard"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
              />
              <TextField
                margin="normal"
                required
                fullWidth
                name="password"
                label="Senha"
                type="password"
                id="password"
                autoComplete="current-password"
                variant="standard"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
              {error && (
                <Typography color="error" variant="body2" align="center" sx={{ mt: 2 }}>
                  {error}
                </Typography>
              )}
              <Button
                type="submit"
                fullWidth
                variant="contained"
                color="primary"
                sx={{ mt: 3, mb: 2, py: 1.5 }}
              >
                Entrar
              </Button>
            </Box>
          </Box>
        </Grid>
      </Grid>
    </Box>
  );
};

export default Login;
