describe('Prueba de login inválido en la app bancaria', () => {

  it('No debe permitir el acceso con credenciales incorrectas', () => {
    cy.visit('https://parabank.parasoft.com/')  // Página bancaria de prueba gratuita

    // Completa el formulario con datos erróneos
    cy.get('input[name="username"]').type('usuario_invalido')
    cy.get('input[name="password"]').type('contraseña_erronea')
    cy.get('input[value="Log In"]').click()

    // Verifica que aparece mensaje de error
    cy.get('#rightPanel')
      .should('contain.text', 'The username and password could not be verified')
  })
})
