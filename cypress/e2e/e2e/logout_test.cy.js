describe('Logout Functionality', () => {

  it('El usuario puede cerrar sesión correctamente', () => {
    // Paso 1: visitar la página y loguearse
    cy.visit('https://www.saucedemo.com/');
    cy.get('[data-test="username"]').type('standard_user');
    cy.get('[data-test="password"]').type('secret_sauce');
    cy.get('[data-test="login-button"]').click();

    // Paso 2: verificar que entró al home
    cy.url().should('include', '/inventory.html');

    // Paso 3: abrir el menú lateral
    cy.get('#react-burger-menu-btn').click();

    // Paso 4: hacer clic en "Logout"
    cy.get('#logout_sidebar_link').click();

    // Paso 5: verificar que volvió al login
    cy.url().should('eq', 'https://www.saucedemo.com/');
  });

});
