
import React from 'react';
import { useNavigate, Link as RouterLink } from 'react-router-dom';
import {
  AppBar,
  Toolbar,
  Typography,
  Box,
  Drawer,
  List,
  ListItem,
  ListItemButton,
  ListItemIcon,
  ListItemText,
  CssBaseline,
  IconButton,
  Avatar,
} from '@mui/material';
import {
  People as PeopleIcon,
  Person as PersonIcon,
  Description as DescriptionIcon,
  Receipt as ReceiptIcon,
  Logout as LogoutIcon,
} from '@mui/icons-material';
import logo from '../../Logo_FC_sem_fundo.png'; // Assuming the logo is still relevant

const drawerWidth = 240;

const navItems = [
  { text: 'Lista de Clientes', icon: <PeopleIcon />, path: '/clientes' },
  { text: 'Perfil', icon: <PersonIcon />, path: '/perfil' },
  { text: 'Receituário', icon: <DescriptionIcon />, path: '/receituario' },
  { text: 'Romaneio', icon: <ReceiptIcon />, path: '/romaneio' },
];

const MainLayout = ({ children }) => {
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem('token');
    navigate('/');
  };

  return (
    <Box sx={{ display: 'flex' }}>
      <CssBaseline />
      <AppBar
        position="fixed"
        sx={{
          width: `calc(100% - ${drawerWidth}px)`,
          ml: `${drawerWidth}px`,
          backgroundColor: 'white',
          color: 'text.primary',
          boxShadow: '0px 1px 4px rgba(0, 0, 0, 0.1)',
        }}
      >
        <Toolbar sx={{ justifyContent: 'flex-end' }}>
          <IconButton>
            <Avatar sx={{ width: 32, height: 32 }} />
          </IconButton>
        </Toolbar>
      </AppBar>
      <Drawer
        sx={{
          width: drawerWidth,
          flexShrink: 0,
          '& .MuiDrawer-paper': {
            width: drawerWidth,
            boxSizing: 'border-box',
            borderRight: 'none',
          },
        }}
        variant="permanent"
        anchor="left"
      >
        <Box sx={{ p: 2, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
          <img src={logo} alt="FibraseCores Logo" style={{ height: 40 }} />
          <Typography variant="h6" sx={{ ml: 1, fontWeight: 'bold' }}>
            FibraseCores
          </Typography>
        </Box>
        <List sx={{ flexGrow: 1 }}>
          {navItems.map((item) => (
            <ListItem key={item.text} disablePadding>
              <ListItemButton component={RouterLink} to={item.path}>
                <ListItemIcon>{item.icon}</ListItemIcon>
                <ListItemText primary={item.text} />
              </ListItemButton>
            </ListItem>
          ))}
        </List>
        <Box>
          <List>
            <ListItem disablePadding>
              <ListItemButton onClick={handleLogout}>
                <ListItemIcon>
                  <LogoutIcon />
                </ListItemIcon>
                <ListItemText primary="Sair" />
              </ListItemButton>
            </ListItem>
          </List>
        </Box>
      </Drawer>
      <Box
        component="main"
        sx={{ flexGrow: 1, bgcolor: 'background.default', p: 3 }}
      >
        <Toolbar /> {/* Spacer for content to be below AppBar */}
        {children}
      </Box>
    </Box>
  );
};

export default MainLayout;
