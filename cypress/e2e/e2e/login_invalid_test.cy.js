describe('Login con credenciales inválidas - SauceDemo', () => {

  it('Debería mostrar mensaje de error al ingresar credenciales incorrectas', () => {
    cy.visit('https://www.saucedemo.com/');

    // Ingresar usuario y contraseña inválidos
    cy.get('[data-test="username"]').type('usuario_invalido');
    cy.get('[data-test="password"]').type('clave_erronea');
    cy.get('[data-test="login-button"]').click();

    // Verificar mensaje de error
    cy.get('[data-test="error"]')
      .should('be.visible')
      .and('contain', 'Username and password do not match');
  });

});
