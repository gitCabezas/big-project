
import React from 'react';
import { Navigate, Outlet } from 'react-router-dom';
import MainLayout from './MainLayout';

const PrivateRoute = () => {
  const isAuthenticated = !!localStorage.getItem('token'); // Check if token exists

  return isAuthenticated ? (
    <MainLayout>
      <Outlet />
    </MainLayout>
  ) : (
    <Navigate to="/" />
  );
};

export default PrivateRoute;

