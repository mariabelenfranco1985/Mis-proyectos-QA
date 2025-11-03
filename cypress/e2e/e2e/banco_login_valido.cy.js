describe('Prueba de login válido en la app bancaria', () => {

  it('Debe permitir el acceso con usuario y contraseña correctos', () => {
    cy.visit('https://parabank.parasoft.com/')   // Página oficial de prueba

    // Escribe credenciales válidas (de prueba)
    cy.get('input[name="username"]').type('john')
    cy.get('input[name="password"]').type('demo')
    cy.get('input[value="Log In"]').click()

    // Verifica que aparece el mensaje de bienvenida o enlace de cuentas
    cy.get('#leftPanel').should('contain.text', 'Accounts Overview')

    // Verifica que el usuario realmente accedió
    cy.url().should('include', '/overview.htm')
  })
})
